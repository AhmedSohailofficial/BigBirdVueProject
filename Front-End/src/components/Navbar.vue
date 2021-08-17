<template>
  <div>
    <div class="Main">
      <div class="MainContainer">
        <div class="logo">
          <img src="images/logoBrand.svg" alt="" />
        </div>
        <div class="buttonBox">
          <div class="buttons">
            <button class="button button1">HOME</button>
            <button class="button button2">PRODUCTS</button>
            <button class="button button3">OFFERS</button>
            <button class="button button4">OUR STORY</button>
            <button class="button button5">MEDIA</button>
            <button class="button button6">CONTACT US</button>
          </div>
        </div>

        <div class="search">
          <div class="searchbox">
            <div class="line">
              <img src="images/line.svg" alt="" />
            </div>
            <div class="SearchText">Search</div>
            <div class="searchicon">
              <i class="fa fa-search"></i>
            </div>
          </div>
        </div>
        <div class="icons">
          <div class="user">
            <img src="images/user.svg" alt="" />
          </div>
          <div class="cart">
            <img src="images/cart.svg" alt="" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.MainContainer {
  display: flex;
}
.logo {
  margin-left: 2%;
}
.buttonBox {
  float: left;
  margin-left: 16%;
}
.buttons {
  margin-top: 2.8%;
}
.button {
  background-color: transparent; /* Green */
  border: none;
  color: black;
  padding: 7px 14px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 2px 1px;
  cursor: pointer;
}
.search {
  display: flex;
  margin-top: 25px;
  margin-left: 15px;
}
.searchbox {
  display: flex;
}
.line {
  margin-top: 10px;
  position: relative;
}
.searchicon {
  position: absolute;
  margin-left: 190px;
}
.SearchText {
  position: absolute;
  margin-left: 5px;
}
.user {
  margin-left: 50%;
  margin-top: 62%;
}
.cart {
  margin-left: 20%;
  margin-top: 60%;
}
.icons {
  display: flex;
  width: auto;
}

@media screen and (max-width: 1280px) {
  .MainContainer {
    display: flex;
    flex-direction: column;
  }

  .logo {
    margin-bottom: 2%;
    text-align: center;
  }
  .buttonBox {
    justify-content: center;
    margin: 0 25%;
  }
  .buttons {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    background-color: transparent;
    margin: auto;
  }
  .button {
    background-color: transparent; /* Green */
    border: none;
    color: black;
    padding: 2px 4px;
    text-align: center;
    justify-content: center;
    text-decoration: none;
    display: flex;
    font-size: 16px;
    margin: 1px 1px;
    cursor: pointer;
  }
  .search {
    background-color: transparent;
    width: 50%;
    margin-left: 25%;
    text-align: center;
  }
  .line {
    margin-top: 10px;
    margin-left: 0%;
  }
  .searchicon {
    text-align: center;
    margin-top: 1px;
    background-color: transparent;
  }
  .SearchText {
    background-color: transparent;
    margin-left: 1%;
  }
  .icons {
    display: flex;
    flex-direction: column;
    text-align: center;
  }
  .user {
    margin-left: 0%;
    margin-top: 2%;
  }
  .cart {
    margin-left: 0%;
    margin-top: 2%;
  }
}
</style>


<script>
export default {
  name: "Navbar",
};
</script>
