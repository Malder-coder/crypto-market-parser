import requests

# Using Cloudflare's public Ethereum RPC endpoint
ETH_RPC_URL = "https://cloudflare-eth.com"

def get_eth_balance(wallet_address):
    """
    Fetches the Ethereum balance of a given address directly from the blockchain
    using public RPC endpoints (No API keys required).
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [wallet_address, "latest"],
        "id": 1
    }
    
    try:
        # Added timeout for RPC stability
        response = requests.post(ETH_RPC_URL, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if 'result' in data:
            # Balance is returned in Wei (hex format), converting to ETH
            balance_wei = int(data['result'], 16)
            balance_eth = balance_wei / (10**18)
            return balance_eth
        else:
            print("Error reading balance from blockchain.")
            return None
            
    except Exception as e:
        print(f"RPC Connection Error: {e}")
        return None

if __name__ == "__main__":
    # Example: Vitalik Buterin's (creator of Ethereum) public wallet address
    test_wallet = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
    
    print(f"Checking balance for: {test_wallet}...")
    balance = get_eth_balance(test_wallet)
    
    if balance is not None:
        print(f"Balance: {balance:.4f} ETH")
