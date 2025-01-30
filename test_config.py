import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
    
print("Telegram Bot Token:", config['apis']['telegram']['bot_token'])
print("RPC URL:", config['blockchain']['rpc_url'])
