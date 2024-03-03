#!python

# This file containing the html must be in a cgi-bin sub-directory.

import cgi
import requests
import cgitb

print("content-type: text/html \n")

print("""
      
<!DOCTYPE html>
<html lang="en-US">
<head>
  <title>Dogesplorer</title>
  <link rel="stylesheet" href="../styles_05.css">
  <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
  <meta charset="UTF-8">
  <meta name="description" content="Doge Blockhain explorer">
  <meta name="keywords" content="doge, crypto, cryptocoin, cryptocurrency, 
  blockchain, block, wallet, address, addres, adress, explorer, explore, 
  search, dogecoin, coin, dog, dogcoin, shiba, inu, shib, sheeb, cheems, bonk,
  litecoin, ltc, trade, trades, trading, hash, transaction, bork, much, money,
  such, currency">
  <meta name="author" content="Dickie">
  <meta name="viewport" content="width=device-width, initial scale=1.0">
</head>

<body>
  <!-- add main page here -->

  <h1>Dogesplorer, the number one Doge explorer on the net!</h1>


    <!-- fake search bar -- or REAL search bar? (function)-->

    <nav class="main_nav">
      <!-- add nav links here -->
      <div class="nav_links">
        <ul class="nav_list">
          <li><a href="https://www.youtube.com/watch?v=hxX9RaTWDnc">link</a></li>
          <li><a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">link</a></li>
          <li><a href="https://www.youtube.com/watch?v=UBsIGF-KZZw">link</a></li>
          <li><a href="https://www.youtube.com/watch?v=Zfr3L0drhS8">link</a></li>
          <li><a href="https://www.youtube.com/watch?v=C3rg4psdHxw">link</a></li>
        </ul>
      </div>


      <div class="search_bar">
        <input class="search_field" type="text" name="query" 
        placeholder=" Enter a wallet address, txn hash, or contract address">
        <button class="search_btn" type="submit">
          <span class="search">search</span></button>
      </div>

    </nav>

    <div class="price_display">
      <div id="doge_tag"><h3>Doge Price: </h3></div>
      <div id="doge_price">Finding latest price...</div>
    </div>



    <script>
      // Function to fetch and update the DOGE price
      function fetchDogePrice() {
          // I have no key for coingecko. Limits fetches to 5 per minute.
          const apiKey = 'NO_KEY';
          const apiUrl = `https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd&apiKey=${apiKey}`;
  
          // Fetch DOGE price from CoinGecko API
          fetch(apiUrl)
              .then(response => response.json())
              .then(data => {
                  const dogePrice = data.dogecoin.usd;
                  console.log('updoot the prooce, ', dogePrice);
                  document.getElementById('doge_price').innerText = `$${dogePrice} USD`;
              })
              .catch(error => {
                  console.error('Error fetching DOGE price:', error);
                  document.getElementById('doge_price').innerText = 'Only 5 price fetches per minute';
              });
      }
  
      // Fetch DOGE price on page load
      fetchDogePrice();
  
      // Refresh DOGE price every 30 seconds
      setInterval(fetchDogePrice, 30000);
  </script>



    <!-- items: search bar, sitemap, graph, news video, news links -->
    <!-- articles: mini graph, current difficulty, number of blocks, recent trades -->
  
      <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>





     
""")


# do some python stuff
# Get form data
form = cgi.FieldStorage()
user_input: str = form.getvalue("user_input", "none")

# declare file path
file_path = "user_message.txt"

# open in append mode. I wanted to get a list
with open(file_path, "a") as file:
    file.write(user_input + "\n")


print("""
      
  
<form method="post" action="cgi_script.py">
  <p>Enter your data: <input type="text" name="user_input"></p>
<p>previously entered data: %s</p>
</form>
</body>
</html>
      
      """ % user_input)