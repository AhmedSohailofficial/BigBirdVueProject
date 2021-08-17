<template>
  <div>
    <div class="border">
      <div class="borderContents">
        <div class="elements">
          <p class="element">Home</p>
          <p class="element">Ready to cook</p>
          <p class="element">Product Page</p>
        </div>
      </div>
    </div>
    <div class="headingbox">
      <div class="heading1">
        <h2 class="subheading1">Welcome to Bigbird</h2>
        <div class="subheading2">
          <h4>
            Get inspired by these awesome ‘About Us’<br />
            page examples from real companies.
          </h4>
          <br />
        </div>
      </div>
      <div>
        <p class="subheading3">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur
          pellentesque neque eget diam posuere porta. Quisque ut nulla at nunc
          vehicula lacinia. Proin adipiscing porta tellus, ut feugiat nibh
          adipiscing sit amet. In eu justo a felis faucibus ornare vel id metus.
        </p>
      </div>
    </div>
    <div class="secondcontainer">
      <div class="mainsecondcontainer">
        <div class="imageofcontainersecond">
          <img
            src="images/Contact/c1.png"
            style="width:550px,height:300px"
            alt=""
          />
        </div>
        <div class="textofcontainersecond">
          <div class="headingsecondcontainer">
            <h1>About Bigbird</h1>
          </div>
          <div class="paragraphofsecondcontainer">
            <p class="textofparagraphsecondcontainer">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur
              pellentesque neque eget diam posuere porta. Quisque ut nulla at
              nunc vehicula lacinia. Proin adipiscing porta tellus, ut feugiat
              nibh adipiscinLorem ipsum dolor sit amet, consectetur adipiscing
              elit. roin adipiscing porta tellus, ut
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="threecontainer">
      <div class="mainthreecontainer">
        <div class="textofcontainerthree">
          <div class="headingthreecontainer">
            <h1>Our Mission</h1>
          </div>
          <div class="paragraphofthreecontainer">
            <p class="textofparagraphthreecontainer">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur
              pellentesque neque eget diam posuere porta. Quisque ut nulla at
              nunc vehicula lacinia. Proin adipiscing porta tellus, ut feugiat
              nibh adipiscinLorem ipsum dolor sit amet, consectetur adipiscing
              elit. roin adipiscing porta tellus, ut
            </p>
          </div>
        </div>
        <div class="imageofcontainerthree">
          <img
            src="images/Contact/c3.png"
            style="width:450px,height:300px"
            alt=""
          />
        </div>
      </div>
    </div>

    <div class="fourcontainer">
      <div class="mainfourcontainer">
        <div class="imageofcontainerfour">
          <img
            src="images/Contact/c3.png"
            style="width:450px,height:300px"
            alt=""
          />
        </div>
        <div class="textofcontainerfour">
          <div class="headingfourcontainer">
            <h1>Our Vission</h1>
          </div>
          <div class="paragraphoffourcontainer">
            <p class="textofparagraphfourcontainer">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur
              pellentesque neque eget diam posuere porta. Quisque ut nulla at
              nunc vehicula lacinia. Proin adipiscing porta tellus, ut feugiat
              nibh adipiscinLorem ipsum dolor sit amet, consectetur adipiscing
              elit. roin adipiscing porta tellus, ut feugiat nibh adipiscing sit
              amet. In eu
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Contact",
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
  .heading1{
      display: flex;
      margin-top: 50px;
  }
  .subheading1{
      margin-left: 170px;
  }
  .subheading2{
      margin-left: 100px;
      position: relative;
      top:5px
  }
  p.subheading3{
    width:60%;
    margin-left: 490px;
  }
  .headingsecondcontainer{
     
      margin-left: 200px;
  }
  p.textofparagraphsecondcontainer{
    width:60%;
  }
  .paragraphofsecondcontainer{
     margin-left: 200px;
  }
  .mainsecondcontainer{
      display: flex;
  }
 .textofcontainersecond{
   position: relative;
   top: 70px;
 }
 .imageofcontainersecond{
     margin-left: 160px;
     margin-top: 50px;
 }






 .headingfourcontainer{
     
    margin-left: 300px;
}
p.textofparagraphfourcontainer{
  width:60%;
}
.paragraphoffourcontainer{
   margin-left: 300px;
}
.mainfourcontainer{
    display: flex;
    margin-bottom: 50px;
}
.textofcontainerfour{
 position: relative;
 top: 70px;
}
.imageofcontainerfour{
   margin-left: 160px;
   margin-top: 50px;
}









.headingthreecontainer{
     
    margin-left: 150px;
}
p.textofparagraphthreecontainer{
  width:60%;
}
.paragraphofthreecontainer{
   margin-left: 150px;
}
.mainthreecontainer{
    display: flex;
}
.textofcontainerthree{
 position: relative;
 top: 70px;
}
.imageofcontainerthree{
   margin-right: 160px;
   margin-top: 50px;
}



@media screen and (max-width: 1280px) {
  .borderContents {
    display: flex;
    margin-left: 17%;
  }
  img{
    height: auto;
    width: 100%;
  }
.subheading1{
    margin-left: 1%;
}
.subheading2{
    margin-left: 4%;
    position: relative;
    top:5px
}
p.subheading3{
  width:90%;
  margin-left: 5%;
}
.imageofcontainersecond{
  
  margin-left: 1%;
  margin-top: 50px;
 }
.headingsecondcontainer{
    text-align: center; 
  margin-left: 20px;
}
p.textofparagraphsecondcontainer{
  width:90%;
}
.paragraphofsecondcontainer{
  
  margin-left: 5%;
}
.mainsecondcontainer{
  display: block;
}
.textofcontainersecond{
position: relative;
top: 30px;
}


.headingthreecontainer{
  text-align: center; 
  margin-left: 20px;
}
p.textofparagraphthreecontainer{
width:90%;
}
.paragraphofthreecontainer{
 margin-left: 5%;
}
.mainthreecontainer{
  display:flex;
  flex-direction: column-reverse;
}
.textofcontainerthree{
position: relative;
top: 30px;
}
.imageofcontainerthree{
  margin-left: 3%;
  margin-top: 50px;
}



.headingfourcontainer{   
  text-align: center; 
  margin-left: 20px;
}
p.textofparagraphfourcontainer{
width:90%;
}
.paragraphoffourcontainer{
 margin-left: 5%;
}
.mainfourcontainer{
  display: block;
  margin-bottom: 25%;
}
.textofcontainerfour{
position: relative;
top: 70px;
}
.imageofcontainerfour{
  margin-left: 3%;
  margin-top: 50px;
}


}
</style>