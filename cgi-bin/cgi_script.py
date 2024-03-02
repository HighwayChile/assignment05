#!python

# This file containing the html must be in a cgi-bin sub-directory.

import cgi

print("content-type: text/html \n")

print("""
      
<!DOCTYPE html>
<html lang="en-US">
<head>
  <title>Dogesplorer</title>
  <link rel="stylesheet" href="../styles_05.css">
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

      <a href="https://www.amazon.com/">link</a>
      <!-- add nav links here -->
      <input type="text" name="query" class="search_field" 
      placeholder=" Enter a wallet address, txn hash, or contract address">

      <button type="submit" class="search_btn">
        <span class="search">search</span></button>
    </nav>





    <!-- make side menus only nav links. -->
    <div id="side_menu">
      <nav>
        <!-- add nav links here -->
      </nav>
    </div>
    





    <!-- items: search bar, sitemap, graph, news video, news links -->
    <!-- articles: mini graph, current difficulty, number of blocks, recent trades -->
  


    <!-- Remove these breaks befor release -->
    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
</body>

<footer>
    <!-- add contact info here -->
</footer>

</html>




     
""")


# do some python stuff
form_data = cgi.FieldStorage()
input_message: str = form_data.getvalue("input_message", "(no message entered)")

print("""

  <p>Previous message: %s</p>
  <p>form</p>
  <form method="post" action="cgi_script.py">
    <p>message: <input type="text" name="input_message" /></p>
  </form>
</body>
</html>
      
""" % input_message)