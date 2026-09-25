# Connecting SignalMind to Azure VM Neo4j (Student Credits Guide)

SignalMind works out-of-the-box using its built-in **In-Memory Graph Engine**. If you want to run the full distributed Neo4j Graph Database on an **Azure Virtual Machine** using your Azure for Students credits ($100 free credit), follow this simple 5-minute setup.

---

## 1. Create your Azure Linux VM
1. Log in to [Azure Portal](https://portal.azure.com/).
2. Click **Create a resource** → **Virtual Machine**.
3. Choose:
   - **Size:** `Standard_B2s` (2 vCPUs, 4 GiB memory — fully covered by student credits).
   - **OS:** `Ubuntu Server 22.04 LTS`.
   - **Authentication:** SSH public key or Password.
4. **Networking (Inbound Port Rules):**
   - Allow `SSH (22)`
   - Add custom inbound port rule for **Neo4j Bolt Protocol**:
     - **Port:** `7687`
     - **Protocol:** `TCP`
     - **Action:** `Allow`
   - (Optional) Allow port `7474` for the web Neo4j Browser UI.

---

## 2. Launch Neo4j with Docker on the Azure VM
SSH into your Azure VM:
```bash
ssh azureuser@<YOUR_AZURE_VM_PUBLIC_IP>
```

Install Docker:
```bash
sudo apt update && sudo apt install -y docker.io
sudo systemctl enable --now docker
```

Run Neo4j container:
```bash
sudo docker run -d \
  --name signalmind-neo4j \
  --restart always \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/YourSecurePassword123! \
  -e NEO4J_PLUGINS='["apoc", "graph-data-science"]' \
  neo4j:5.15-community
```

---

## 3. Update `.env` in SignalMind
In `e:\SignalMind\.env`:
```env
# Azure VM Neo4j Settings
NEO4J_URI=bolt://<YOUR_AZURE_VM_PUBLIC_IP>:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=YourSecurePassword123!

# Groq API Key (Optional for Llama 3 70B profile generation)
GROQ_API_KEY=gsk_your_groq_key_here
GROQ_MODEL=llama3-70b-8192

ENVIRONMENT=development
PORT=8000
```

---

## 4. Run SignalMind
```bash
.\venv\Scripts\python.exe main.py
```
Open `http://localhost:8000/app` — the status indicator in the top navbar will automatically show:
`Azure VM Neo4j: connected`!
