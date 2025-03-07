// PACKAGES
require("dotenv").config();
const { ethers } = require("ethers");
const mysql = require('mysql2');

// CONSTANTS

// env. variables
const privateKey = process.env.PRIVATE_KEY;
const alchemyUrl = process.env.ALCHEMY_API_URL;
const dbPassword = process.env.DB_PASSWORD;

// Connect to Ethereum
const provider = new ethers.JsonRpcProvider(alchemyUrl);
const wallet = new ethers.Wallet(privateKey, provider);

// initiate the connection
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: dbPassword,
    database: "blockchain_fraud"
});

// Maximum transactions to save (as to not kill my PC)
const MAX_TRANSACTIONS = 1000000;

// Count the current number of transactions
async function getTransactionCount() {
    return new Promise((resolve, reject) => {
        db.query("SELECT COUNT(*) AS count FROM transactions", (err, results) => {
            if (err) reject(err);
            else resolve(results[0].count);
        });
    });
}

// save the transactions to mysql
async function saveToDatabase(tx) {
    const query = `INSERT INTO transactions (hash, sender, recipient, value, gas_used, gas_price)
                   VALUES (?, ?, ?, ?, ?, ?)
                   ON DUPLICATE KEY UPDATE value=value;`;

    const values = [
        tx.hash,
        tx.from,
        tx.to ? tx.to : 'Contract Creation',
        tx.value ? ethers.formatEther(tx.value) : '0',
        tx.gasLimit ? tx.gasLimit.toString() : '0',
        tx.gasPrice ? ethers.formatUnits(tx.gasPrice, 'gwei') : '0'
    ];

    db.query(query, values, (err, result) => {
        if (err) console.error("MySQL Error:", err.message);
        else console.log(`Transaction saved: ${tx.hash}`);
    });
}

// Function to fetch transactions from multiple blocks
async function fetchTransactionsFromBlocks(startBlock, numBlocks) {
    for (let i = 0; i < numBlocks; i++) {
        let blockNumber = startBlock - i;
        console.log(`Fetching transactions from Block #${blockNumber}`);

        try {
            const block = await provider.getBlock(blockNumber);
            if (!block || !block.transactions.length) continue;

            console.log(`Found ${block.transactions.length} transactions in Block #${blockNumber}`);

            for (let j = 0; j < block.transactions.length; j++) {
                const txHash = block.transactions[j];
                const tx = await provider.getTransaction(txHash);
                if (tx) await saveToDatabase(tx);
            }
        } catch (error) {
            console.error(`ERROR fetching block #${blockNumber}:`, error);
        }
    }
}

// Function to continuously fetch transactions until some limit is reached
async function continuousFetch() {
    let latestBlock = await provider.getBlockNumber();
    
    while (true) {
        let txCount = await getTransactionCount(); // wait for 
        console.log(`Current transaction count: ${txCount}`);

        // For when we hit the set maximum
        if (txCount >= MAX_TRANSACTIONS) { 
            console.log("Reached transaction limit. Stopping script.");
            db.end(); // Close database connection
            process.exit(0); // Exit script
        }

        console.log("\nFetching the next set of transactions...");
        await fetchTransactionsFromBlocks(latestBlock, 10); // Fetch 10 blocks at a time
        latestBlock -= 10; // Move back 10 blocks
        await new Promise(resolve => setTimeout(resolve, 5000)); // Wait 5 sec before next batch
    }
}

continuousFetch();
