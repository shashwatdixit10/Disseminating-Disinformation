chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.url) {
      console.log("hello");
      chrome.tabs.executeScript(tabId, { file: 'script.js' }, () => {
        console.log('Content script injected.');
        });
    }
  });