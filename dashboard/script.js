const apiUrl = "https://ham4q79pr9.execute-api.us-east-1.amazonaws.com/prod/GetInventoryData";

async function fetchInventoryData() {
  try {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    console.log("Fetched data:", data);

    const inventoryDiv = document.getElementById("inventory-data");
    inventoryDiv.innerHTML = "";

    data.forEach(item => {
      const itemDiv = document.createElement("div");
      itemDiv.textContent = `📦 ${item.name} - Stock: ${item.stock}, Reorder Point: ${item.reorder_point}`;
      inventoryDiv.appendChild(itemDiv);
    });
  } catch (error) {
    console.error("Error fetching inventory data:", error);
    const inventoryDiv = document.getElementById("inventory-data");
    inventoryDiv.textContent = "⚠️ Error fetching data.";
  }
}

fetchInventoryData();
