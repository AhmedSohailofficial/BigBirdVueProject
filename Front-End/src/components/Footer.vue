<template>
  <div>
    <div class="MainBlock">
      <div class="footer1">
        <div class="footercontainer">
          <div class="MainHeading">
            <div class="MainHeadingText">
              <h1>Stay on Top of Things</h1>
            </div>
            <div class="innerText">
              <p>
                Sign up and get lattest update Integer quis tempor orci.<br />
                uspendisse potenti. get uspendisse potenti Sign up and.
              </p>
            </div>
          </div>

          <div class="formimputemailclass">
            <form class="formimputemail">
              <input
                type="email"
                id="email"
                name="email"
                placeholder="  Enter email adress"
                class="inputemail"
              />
              <button type="submit" class="inputemailbutton">
                Subscribe
              </button>
            </form>
          </div>
        </div>
      </div>
      <div class="footer2">
        <div class="logo">
          <img src="images/logoBrand.svg" alt="" />
          <div class="logos">
            <div class="facebook">
              <img src="images/icons/facebook.svg" alt="" />
            </div>
            <div class="twitter">
              <img src="images/icons/twitter.svg" alt="" />
            </div>
            <div class="linkdin">
              <img src="images/icons/linkdin.svg" alt="" />
            </div>
          </div>
        </div>
        <div class="Wrapper">
          <div class="Products">
            <h1>Products</h1>
            <div>
              <h6>Home</h6>
              <h6>Group Profile</h6>
              <h6>Big Begining</h6>
              <h6>Production</h6>
              <h6>Customer Care</h6>
              <h6>Careers</h6>
            </div>
          </div>
          <div class="Products2">
            <h1>Products</h1>
            <div>
              <h6>Processed Chicken</h6>
              <h6>Ready to Cook</h6>
              <h6>Production</h6>
              <h6>Fully Cooked</h6>
            </div>
          </div>
          <div class="More">
            <h1>More</h1>
            <div>
              <h6>Location</h6>
              <h6>2-A Ahmad Block New Garden town <br />Lahore Pakistan</h6>
              <br />
              <h6>
                UAN <br />
                +92-42-111-244-111
              </h6>
            </div>
          </div>

          <div class="ContactDetails">
            <div>
              <h6>Phone</h6>
              <h6>042-35835373 042-3587512-14 <br />Lahore Pakistan</h6>
              <br />
              <h6>
                Fax <br />
                +92-4235860519
              </h6>
            </div>
          </div>
        </div>
      </div>
      <div class="footer3">
        <h1 class="headerText1">
          All Rights Reserved. Powerd by alchemative
        </h1>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Footer",
};
</script>
<style scoped>
.footer1 {
  height: 140px;
  background-color: #fafafa;
}
.footer2 {
  height: auto;
  background-color: white;
  display: flex;
}
.MainHeadingText {
  color: black;
  margin-left: 30px;
  position: relative;
  top: 20px;
}
.innerText {
  margin-left: 30px;
  position: relative;
  top: 20px;
  text-align: justify;
  font-size: 12px;
}
.inputemail {
  margin-left: 800px;
  height: 40px;
  width: 20%;
  border: 1px #dcdcdc;
}
.inputemailbutton {
  height: 40px;
  width: 8%;
  margin-left: 40px;
  border: none;
  color: white;
  background-color: #bc2455;
}
.footer3 {
  height: 40.5px;
  background-color: #fafafa;
}
.logo {
  position: relative;
  top: 20px;
}
.logos {
  display: flex;
}
.twitter {
  margin-left: 25px;
}
.linkdin {
  margin-left: 25px;
}
.Wrapper {
  margin-top: 30px;
  display: flex;
}
.Products {
  margin-left: 150px;
}
.Products2 {
  margin-left: 150px;
}
.More {
  margin-left: 150px;
}
.ContactDetails {
  margin-left: 150px;
  position: relative;
  top: 45px;
}

.headerText1 {
  position: relative;
  top: 8px;
  text-align: center;
  padding: 7px;
  color: black;
  font-size: 11px;
}
.formimputemail {
  position: relative;
  top: -30px;
}

@media screen and (max-width: 1280px) {
  .footer1 {
    height: 225px;
    background-color: #fafafa;
  }
  .footercontainer {
    display: flex;
    flex-direction: column;
  }
  .MainHeading {
    margin-left: 10%;
    text-align: center;
  }
  .innerText {
    text-align: center;
  }
  .formimputemailclass {
    position: relative;
    top: 90px;
    margin-left: 10%;
    text-align: center;
  }
  .inputemail {
    margin-left: 40px;
    height: 40px;
    width: 200px;
    border: 1px #dcdcdc;
  }
  .inputemailbutton {
    height: 40px;
    width: 103px;
    border: none;
    color: white;
    background-color: #bc2455;
  }
  .footer2 {
    height: auto;
    background-color: white;
    display: block;
  }
  .logo {
    margin-left: 45%;
  }
  .logos {
    display: flex;
  }
  .twitter {
    margin-left: 25px;
  }
  .linkdin {
    margin-left: 25px;
  }
  .Wrapper {
    margin-top: 30px;
    display: grid;
    grid-template-columns: 50% 50%;
  }
  .Products {
    margin-left: 20%;
  }
  .Products2 {
    margin-left: 40%;
  }
  .More {
    margin-left: 20%;
  }
  .ContactDetails {
    margin-left: 40%;
    position: relative;
    top: 45px;
  }
}
</style>
