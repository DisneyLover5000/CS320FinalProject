const clear = document.getElementById("clear");
const list = document.getElementById("list");
function addItem() {
  const currentItem = document.getElementsByName('name');
  const listItem = document.getElementById.innerHTML("write");
  listItem.innerHTML = currentItem;
  list.appendChild(listItem);
}
clear.onclick = function() {
  list.innerHTML = "";
} 