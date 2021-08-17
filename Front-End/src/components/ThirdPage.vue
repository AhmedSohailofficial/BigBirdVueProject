<template>
  <div>
    <Header />
    <Navbar />

    <div class="border">
      <div class="borderContents">
        <div class="elements">
          <p class="element">Home</p>
          <p class="element">Ready to cook</p>
          <p class="element">Product Page</p>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="bsimages">
        <div class="containerimages">
          <div class="shortimages">
            <img src="/images/item/i1.png" alt="" class="highlightImage" />
            <img src="/images/item/i1.png" alt="" class="NonhighlightImage" />
            <img src="/images/item/i1.png" alt="" class="NonhighlightImage" />
          </div>
        </div>
      
        <div class="mainImagecontainer">
            
            <div class="mainimage">
            
          <img :src="src='http://127.0.0.1:8000'+OneProduct[this.ID-1].image"   :style="{height:h, width:w }" alt="">
           </div> 
        </div>
      </div>
      <div class="itemdetails">
        <div class="itemdetailcontainer">
          <dv class="itemcontainertext">
            <p>Fresh Chicken &nbsp; SKU: FPR-1116</p>
            <h1>500 pkr</h1>
            <br />
            <p>
              This Product is available at following locations for pickup.
              <br />
              Category: Ready to Cook,
            </p>
            <br />
          </dv>
          <div class="FormContainer">
            <div class="ContainerB">
              <button class="plus">+</button>
              <span class="spantext"> 1 </span>
              <button class="minus">-</button>
            </div>
            <div class="dropdownMenu">
              <form class="dropdownClass">
                <select name="cars" id="cars" class="dropdownselect">
                  <optgroup label="Swedish Cars">
                    <option value="volvo">Choose</option>
                    <option value="saab">Saab</option>
                  </optgroup>
                </select>
              </form>
            </div>
          </div>
          <div class="AddtoChartButton">
            <br />
            <button class="cssofAddtoChart">Add to Chart</button>
          </div>
          <div class="threedropdown">
            <div class="Description">
              <form class="dropdownClassDescription">
                <select name="cars" id="cars" class="dropdownselectDescription">
                  <optgroup label="Swedish Cars">
                    <option value="volvo">Description</option>
                    <option value="saab">Saab</option>
                  </optgroup>
                </select>
              </form>
            </div>
            <div class="Ingredients">
              <form class="dropdownClassIngredients">
                <select name="cars" id="cars" class="dropdownselectIngredients">
                  <optgroup label="Swedish Cars">
                    <option value="volvo">Ingredients</option>
                    <option value="saab">Saab</option>
                  </optgroup>
                </select>
              </form>
            </div>
            <div class="Reviews">
              <form class="dropdownClassReviews">
                <select name="cars" id="cars" class="dropdownselectReviews">
                  <optgroup label="Swedish Cars">
                    <option value="volvo">Reviews</option>
                    <option value="saab">Saab</option>
                  </optgroup>
                </select>
              </form>
            </div>
            <div class="Share">
              <div class="textShare">
                <p>Share:</p>
                <img
                  src="/images/icons/whatsapp.png"
                  class="whatsappicon"
                  alt=""
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="ReviewItem">
      <div class="ReviewItemText">
        <h1>Review Item</h1>
      </div>

      <div class="ReviewItemsCard">
        <div v-for="Review in Reviews" :key="Review.SubText">
          <div class="card">
            <div class="cardBox">
              <div class="cardimage">
                <img
                  :src="Review.image"
                  style="height: 100px, width: 100px"
                  alt=""
                />
              </div>
              <div class="card1textbox">
                <div class="cardHeading"></div>
                <h3>{{ Review.MainText }}</h3>
                <div class="cardstar">
                  <img src="/images/RatingStar/Star.svg" alt="" />
                  <img src="/images/RatingStar/Star.svg" alt="" />
                  <img src="/images/RatingStar/Star.svg" alt="" />
                  <img src="/images/RatingStar/Star.svg" alt="" />
                  <img src="/images/RatingStar/Star.svg" alt="" />
                </div>
              </div>
              <div class="subText">
                <p>
                  {{ Review.SubText }}
                </p>
                <h6>Name</h6>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="ReviewItem">
      <div class="ReviewItemText">
        <h1>You May Also Like</h1>
      </div>

      <div class="ReviewItemsCard">
        <div v-for="Like in Likes" :key="Like.SubText">
          <div class="card">
            <div class="cardBox">
              <div class="cardimage">
                <img class="cardimageLike" :src="Like.image" style=" height: 150px, width: 200px" alt="" />
              </div>
              <br />
              <div class="card1textbox">
                <div class="cardHeading"></div>

                <p>{{ Like.MainText }}</p>
                <div class="cardstar">
                  <img src="/images/RatingStar/Star.svg" alt="" />
                  <img src="/images/RatingStar/Star.svg" alt="" />
                  <img src="/images/RatingStar/Star.svg" alt="" />
                  <img src="/images/RatingStar/Star.svg" alt="" />
                  <img src="/images/RatingStar/Star.svg" alt="" />
                </div>
              </div>

              <div class="subText">
                <br />
                <p>{{ Like.SubText }}</p>
                <br />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <Footer />
  </div>
</template>
<script>
import Header from "./Header.vue";
import Navbar from "./Navbar.vue";
import Footer from "./Footer.vue";
import axios from "axios";
export default {
  name: "OneProduct",
  components: {
    Header,
    Navbar,
    Footer,
  },
  data() {
    return {
      "OneProduct":null,
      ID: this.$route.params.id,
      Likes: [],
      Reviews: [],
      h:'400px',
      w:'483px'
    };
   
  },

  
  created() {
    try{
      axios
      .get("http://127.0.0.1:8000/api/SecondProducts/")
      .then((response) => (this.OneProduct=response.data,
      console.log("this is from response"),
      console.log(response.data),
      console.log("this is from oneproduct"),
      console.log(this.OneProduct)
  
      ) );
    }
    catch(error)
    {
      console.log(error)
    }

    this.Likes = [
      {
        id: 1,
        image: "/images/FeaturedProducts/d1.png",
        MainText: "Freh Chicken",
        SubText: "500 Pkr",
      },
      {
        id: 2,
        image: "/images/FeaturedProducts/d1.png",
        MainText: "Freh Chicken",
        SubText: "500 Pkr",
      },
      {
        id: 3,
        image: "/images/FeaturedProducts/d1.png",
        MainText: "Freh Chicken",
        SubText: "500 Pkr",
      },
      {
        id: 4,
        image: "/images/FeaturedProducts/d1.png",
        MainText: "Freh Chicken",
        SubText: "500 Pkr",
      },
    ],
      (this.Reviews = [
        {
          id: 1,
          image: "/images/FeaturedProducts/d1.png",
          MainText: "Best Quality",
          SubText:
            "Ea eu id quis ad sint. Veniam pariatur adipisicing aliqua pariatur ut nulla cillum",
        },
        {
          id: 2,
          image: "/images/FeaturedProducts/d1.png",
          MainText: "Best Quality",
          SubText:
            " Ea eu id quis ad sint. Veniam pariatur adipisicing aliqua pariatur ut nulla cillum",
        },
        {
          id: 3,
          image: "/images/FeaturedProducts/d1.png",
          MainText: "Best Quality",
          SubText:
            " Ea eu id quis ad sint. Veniam pariatur adipisicing aliqua pariatur ut nulla cillum",
        },
        {
          id: 4,
          image: "/images/FeaturedProducts/d1.png",
          MainText: "Best Quality",
          SubText:
            " Ea eu id quis ad sint. Veniam pariatur adipisicing aliqua pariatur ut nulla cillum",
        },
      ]);
  },
   computed:{

      OneProductImage(){
        return this.OneProduct.filter((one)=> one.id === this.ID)
      }
    }
};
</script>
<style scoped>
.border {
  width: 100%;
  height: 59px;
  background-color: #fafafa;
}
.borderContents {
  display: flex;
  margin-left: 150px;
}
.elements {
  display: flex;
  margin-top: 20px;
}
.element {
  margin-left: 25px;
}
.NonhighlightImage {
  opacity: 0.2;
  margin-bottom: 20px;
}
.container {
  display: flex;
}
.bsimages {
  display: flex;
}
.shortimages {
  display: grid;
  width: 75px;

  margin-left: 180px;
  margin-top: 40px;
}
.highlightImage {
  margin-bottom: 20px;
}
.mainImagecontainer {
  margin-top: 50px;
  height: 440px;
  width: 501px;
  margin-left: 40px;
  background-color: #fafafa;
  /* background-color: white; */
}
.mainimage {
  position: relative;
  mix-blend-mode: multiply;
  top: 18px;
  right: -20px;
}
.itemdetailcontainer {
  margin-top: 50px;
  margin-left: 30px;
  background-color: white;
}
.plus {
  background: none;
  border: none;
  position: relative;
  top: 16%;
  left: 5%;
}
.spantext {
  margin-left: 20%;
  margin-right: 20%;
  position: relative;
  top: 7.5px;
}
.minus {
  background: none;
  border: none;
  position: relative;
  top: 16%;
  left: 5%;
}
.ContainerB {
  border-radius: 60px;
  width: 110px;
  height: 40px;
  border: 1px solid black;
}

.dropdownselect {
  border: 1px solid black;
  width: 150px;
  height: 40px;
  background-color: none;
  background: none;
  margin-left: 65px;
}
.FormContainer {
  display: flex;
}
.cssofAddtoChart {
  border-radius: 56px;
  border: none;
  width: 325px;
  height: 40px;
  color: white;
  background-color: #bc2455;
  margin-bottom: 20px;
}
.dropdownselectDescription,
.dropdownselectIngredients,
.dropdownselectReviews {
  margin-top: 1px;
  border: none;
  border-bottom: 0.5px solid black;
  width: 320px;
  height: 40px;
  background: none;
}
.dropdownselectReviews {
  border-bottom: none;
}
.textShare {
  display: flex;
}
.whatsappicon {
  margin-left: 20px;
  margin-top: 16px;
  height: 18px;
  width: 18px;
}
.ReviewText {
  text-align: center;
  position: relative;
  top: 80px;
  margin-top: 200px;
}
.ReviewItems {
  background-color: #fafafa;
  height: 521px;
  width: 100%;
  margin-bottom: 100px;
}
.ReviewItemText {
  text-align: center;
}

.ReviewImagesContainer {
  display: flex;
  margin-top: 150px;
}

.dver2box {
  margin-top: 100px;
  display: flex;
  justify-content: center;
  height: 265px;
}

.cardimageLike {
  margin: 5% 15%;
}
.leftarrow {
  position: relative;
  top: 130px;
  left: 100px;
}
.rightarrow {
  position: relative;
  top: 130px;
  right: 100px;
}
img {
  max-width: 100%;
  height: auto;
}
.cards {
  height: auto;
  width: fit-content;
  background-color: blue;
}
.paragraph {
  width: 40%;
}

.YouMayAlsoLike {
  margin-bottom: 100px;
}
.YouMayAlsoLikeText {
  text-align: center;
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
  flex: 0 1 calc(25% - 1em);
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
  margin-top: 8%;
}
@media screen and (max-width: 1280px) {
  .shortimages {
    display: grid;
    width: 75px;
    margin-left: 18%;
    margin-top: 40px;
  }
  .whatsappicon {
    margin-left: 20px;
    margin-top: 0px;
  }
  .bsimages {
    justify-content: center;
  }
  .itemdetails {
    text-align: center;
  }
  .container {
    display: block;
  }
  .FormContainer {
    justify-content: center;
  }

  .textShare {
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  .ReviewText {
    text-align: center;
    position: relative;
    top: 80px;
    margin-top: 200px;
  }
}
@media screen and (max-width: 800px) {
  .ReviewItemsCard {
    width: 50%;
    margin: 0 auto;
  }
}
</style>
