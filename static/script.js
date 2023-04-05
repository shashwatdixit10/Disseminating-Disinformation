const urlInput = document.querySelector('.url-input');

chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
  const activeTab = tabs[0];
  const url = activeTab.url;

  urlInput.value = url;
});
