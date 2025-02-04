<script setup>
import ApiForm from './fruits_content/ApiForm.vue'
import FruitsList from './fruits_content/FruitsList.vue'
</script>

<template>
  <div class="xl:w-3/4 mx-auto grid grid-cols-1 lg:grid-cols-2 max-lg:gap-10 pt-10">
    <FruitsList
      :selectedFruit="selectedFruit"
      @updateSelectedFruit="updateSelectedFruit"
    ></FruitsList>
    <ApiForm :selectedFruit="selectedFruit" @clearSelectedFruit="clearSelectedFruit"></ApiForm>
  </div>
</template>

<script>
export default {
  name: 'FruitsContainer',
  data() {
    return {
      selectedFruit: null,
    }
  },
  methods: {
    updateSelectedFruit(selectedFruit) {
      this.selectedFruit = selectedFruit
    },
    clearSelectedFruit() {
      this.selectedFruit = null
    },
  },
}
</script>
