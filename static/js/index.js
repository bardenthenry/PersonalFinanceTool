// 取得按鈕和 sidebar 的 DOM 元素
const sidebarToggle = document.getElementById('sidebar-toggle');
const sidebar = document.getElementById('sidebar');

// 為按鈕加上點擊事件監聽器
sidebarToggle.addEventListener('click', () => {
  // 切換 sidebar 元素的 'collapsed' class
  sidebar.classList.toggle('collapsed');
  if (sidebarToggle.innerText == '收起'){
    sidebarToggle.innerText = '展開'
  } else {
    sidebarToggle.innerText = '收起'
  }
});
