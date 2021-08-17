<template>
  <div class="MainBox">
    <Navbar />
    <div class="MainBoxContainer">
      <div class="Maintext">
        <div>
          <h4>__ Introducing</h4>
        </div>
        <div>
          <h1>Chicken Jalapeno</h1>
        </div>
        <div>
          Bamboo is a furnitutre company that provide quality product to <br />
          meet your indoor or outdoor furniture needs.
        </div>
        <div>__ Read More</div>
      </div>
      <div class="imageMainContainer">
        <img
          src="images/LandingPage/Main/dish.png"
          class="imageMain"
          alt=""
        />
      </div>
    </div>
  </div>
</template>
<script>
import Navbar from "./Navbar.vue";
export default {
  name: "MainMenu",
  components: { Navbar },
};
</script>
<style scoped>
.MainBox {
  background-color: #f3efe2;
  height: 567.1px;
  width: 100%;
}

.Maintext {
  margin-left: 120px;
  margin-top: 62px;
}
.imageMain {
  mix-blend-mode: multiply;
  position: absolute;
  width: 750.95px;
  height: 550.71px;
  left: 530px;
  top: 87.8px;
}
@media screen and (max-width: 1280px) {
  .MainBox {
    background-color: #f3efe2;
    height: 967.1px;
    width: 100%;
    text-align: center;
  }
  .MainBoxContainer {
    display: block;
  }

  img.imageMain {
    width: 450.95px;
    height: auto;
    position: relative;
    left: 2%;
    top: 0px;
  }
}
</style>
