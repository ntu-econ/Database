---
title: '404 - 你進到不該進的地方了：Ｐ'
date: 2023-09-04 08:10:00
permalink: /404.html
---

## 這是一個不存在的頁面

很抱歉，你目前存取的頁面並不存在。
5秒後將會自動返回首頁。
或是 **[按此](https://ntu-econ.github.io/)** 返回首頁。

Sorry, this page does not exist.
We will redirect you back to the homepage 5 seconds later.
Or you can **[Click](https://ntu-econ.github.io/)** to return the homepage.

<script>
let countTime = 5;

function count() {
  
  document.getElementById('timeout').textContent = countTime;
  countTime -= 1;
  if(countTime === 0){
    location.href = 'https://ntu-econ.github.io/';
  }
  setTimeout(() => {
    count();
  }, 1000);
}

count();
</script>
