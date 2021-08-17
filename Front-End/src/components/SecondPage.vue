<template>
  <div>
    <Header />
    <Navbar />
    <div class="filter">
      <div class="imageAndText">
        <div class="imgtext">
          <img src="images/icons/filter.png" alt="" />
        </div>
        <div class="filtertext">
          <p>Filter</p>
        </div>
      </div>
      <div class="bars">
        <div class="barstwo">
          <table style="width: 2.5%">
            <tr>
              <td>abc</td>
              <td>abc</td>
            </tr>
          </table>
        </div>
        <div class="barsthree">
          <table style="width: 5%">
            <tr>
              <td>abc</td>
              <td>abc</td>
              <td>abc</td>
            </tr>
          </table>
        </div>
        <div class="barsfour">
          <table style="width: 10%">
            <tr>
              <td>abc</td>
              <td>abc</td>
              <td>abc</td>
              <td>abc</td>
            </tr>
          </table>
        </div>
      </div>
      <div>
        <select name="cars" id="cars" class="dropdown">
          <optgroup label="Featured">
            <option value="Featured">Featured</option>
            <option value="audi">Audi</option>
          </optgroup>
        </select>
      </div>
    </div>
    <div class="ReviewItemsCard">
      
      <!-- <div v-for="Product in Products.data" :key="Product.id">
       <p>{{Product.image}}</p>
      </div> -->
      
      <div v-for="Product in Products" :key="Product.SubText">
        <div class="card">
          <router-link :to="{name:'OneProduct',params:{ id :Product.id}}" style="text-decoration:none ; color:black">
           
          <div class="cardBox">
            <div class="cardimage">
              <img
                v-bind:src=" 'http://127.0.0.1:8000'+Product.image"
                style=" height: 100px, width: 100px"
                alt=""
              />
            </div>
            <div class="card1textbox">
              <div class="cardHeading"></div>
              <p>{{ Product.MainText }}</p>
              <div class="cardstar">
                <img src="images/RatingStar/Star.svg" alt="" />
                <img src="images/RatingStar/Star.svg" alt="" />
                <img src="images/RatingStar/Star.svg" alt="" />
                <img src="images/RatingStar/Star.svg" alt="" />
                <img src="images/RatingStar/Star.svg" alt="" />
              </div>
            </div>
            <div class="subText">
              <p>{{ Product.SubText }}</p>
            </div>
          
          </div>
          </router-link>
        </div>
      </div>
    </div>

    <div class="finisher">
      <br />
      <!-- <p class="finisherline">
        ______________________________________________________________________________________________________________________________________________
      </p> -->
      <hr />
      <br />
      <p><span style="color: #bc2455">1</span> &nbsp; 2 &nbsp; Next</p>
    </div>
    <Footer />
  </div>
</template>

<script>
import axios from "axios"
import Header from "./Header.vue";
import Navbar from "./Navbar.vue";
import Footer from "./Footer.vue"
export default {
  name: "Products",
  components: {
    Header,
    Navbar,
    Footer,
  },
  data() {
    return {
      Products:null,
      };
  },
  mounted () {
    
    try{
    axios
      .get('http://127.0.0.1:8000/api/SecondProducts/')
      .then(response => (this.Products = response.data,console.log(response.data) )
      )
       
      console.log('Hi')
    }
    catch(error)
    {
      console.log(error)
    }
     
  },

};
</script>
<style>
.mainnavBar {
  width: 100%;
  height: 40vh;
  background-color: #fafafa;
}
.NavText {
  text-align: center;
  position: relative;
  top: 45px;
}
.imageAndText {
  display: flex;
}

.finisher {
  text-align: center;
  margin-bottom: 30px;
}
.dropdown {
  border-radius: 56px;
  border: 1px solid black;
  width: 150px;
  height: 30px;
  text-align: center;
  margin-left: 220px;
  margin-top: 50px;
}

.filter {
  display: flex;
}
.bars {
  display: flex;
  margin-left: 320px;
  margin-top: 50px;
  justify-content: center;
}
table {
  border: 1px solid black;
}
td,
th {
  background-color: black;
}

.imgtext {
  width: 20px;
  height: 20px;
}
.imgtext {
  display: flex;
  margin-left: 120px;
  margin-top: 50px;
}
.barstwo {
  margin-left: 20px;
  height: 20px;
  opacity: 0.2;
}
.barsthree {
  margin-left: 20px;
  height: 20px;
  opacity: 0.2;
}
.barsfour {
  margin-left: 20px;
}
.filtertext {
  margin-left: 10px;
  margin-top: 35px;
}
.ReviewItemsCard {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 0.1fr));
  grid-gap: 0px;
  grid-column: 15rem;
  justify-content: center;
  align-items: center;
}
.card {
  margin-bottom: 30px;
  /* flex: 0 1 calc(25% - 1em); */
  background-color: fafafa;
  width: 90%;
}
.card1textbox {
  display: flex;
}
.subText {
  width: 60%;
}
.cardstar {
  margin-left: 19%;
  margin-top: 5%;
}

@media screen and (max-width: 992px) {
  .mainnavBar {
    width: 100%;
    height: 80vh;
    background-color: #fafafa;
  }
  .filter {
    display: block;
  }
  .imageAndText {
    display: block;
  }
  .filtertext {
    text-align: center;
  }
  .bars {
    display: flex;
    margin-top: 50px;
    margin-left: 0px;
  }
  table {
    border: 1px solid black;
  }
  td,
  th {
    background-color: black;
  }

  .imgtext {
    display: flex;
    margin-left: 45%;
    margin-right: 0;
    margin-top: 20px;
  }
  .barstwo {
    margin-left: 20px;
    height: 20px;
    opacity: 0.2;
  }
  .barsthree {
    margin-left: 20px;
    height: 20px;
    opacity: 0.2;
  }
  .barsfour {
    margin-left: 20px;
  }
  .filtertext {
    margin-left: 10px;
  }
  .dropdown {
    border-radius: 56px;
    border: 1px solid black;
    width: 150px;
    height: 30px;
    text-align: center;
    margin-left: 38%;
    margin-top: 50px;
  }
  .dbox {
    display: inline-block;
    margin-top: 60px;
    height: 200px;
    margin-left: 30%;
  }
  .d1box {
    width: 10%;

    background-color: #fcfaf8;
  }
  .d1textbox {
    display: flex;
  }

  .d1star,
  .d2star,
  .d3star,
  .d4star {
    margin-left: 70px;
    display: flex;
  }
  .finisherline {
    display: none;
  }
  .finisher {
    text-align: center;
    margin-top: 80px;
  }
  @media screen and (max-width: 800px) {
    .ReviewItemsCard {
      width: 50%;
      margin: 0 auto;
    }
  }
}
</style>
