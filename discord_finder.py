import requests

def find_new_discords():
    """
    Fetches newly created crypto pools from GeckoTerminal API
    and filters out projects that have a Discord community link.
    """
    print("Scanning newly created crypto pools for Discord links...")
    
    # Getting newly created pools on the Arbitrum network (very active for new tokens)
    url = "https://api.geckoterminal.com/api/v2/networks/arbitrum/new_pools"
    headers = {"Accept": "application/json;version=20230302"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        pools = data.get("data", [])
        found_any = False
        
        for pool in pools:
            attributes = pool.get("attributes", {})
            name = attributes.get("name", "Unknown Token")
            
            # Extracting website or social links if available
            # GeckoTerminal sometimes provides token metadata endpoints
            # For demonstration, we simulate structural scanning of the target attributes
            websites = attributes.get("websites", [])
            discord_url = None
            
            for site in websites:
                if "discord.gg" in site or "discord.com" in site:
                    discord_url = site
                    break
            
            if discord_url:
                print(f"✅ Token: {name} | Discord: {discord_url}")
                found_any = True
                
        if not found_any:
            print("\nScan finished. No direct Discord links embedded in the raw pool metadata.")
            print("Tip: Most micro-caps list their Telegram/Twitter first. Expand search to Twitter scraping next.")
            
    except Exception as e:
        print(f"API Error: {e}")

if __name__ == "__main__":
    find_new_discords()
