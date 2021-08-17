<template>
  <div >
    <div >
      <router-link to="/">Landing Page</router-link> |
      <router-link to="/products">Second</router-link> | 
      <router-link to="/contact">Fourth</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
 margin: 0;
 padding: 0;
 box-sizing: border-box;
}

</style>
