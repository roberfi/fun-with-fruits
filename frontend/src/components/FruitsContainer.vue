<script setup>
import ApiForm from './fruits_content/ApiForm.vue'
import FruitsList from './fruits_content/FruitsList.vue'
</script>

<template>
  <div class="xl:w-3/4 mx-auto grid grid-cols-1 lg:grid-cols-2 max-lg:gap-10 pt-10">
    <FruitsList
      :fruits="fruits"
      :selectedFruit="selectedFruit"
      @selectFruit="selectFruit"
    ></FruitsList>
    <ApiForm
      :selectedFruit="selectedFruit"
      @deselectFruit="deselectFruit"
      @addFruit="addFruit"
      @updateFruit="updateFruit"
      @deleteFruit="deleteFruit"
    ></ApiForm>
  </div>
</template>

<script>
export default {
  name: 'FruitsContainer',
  data() {
    return {
      fruits: [],
      selectedFruit: null,
    }
  },
  methods: {
    async fetchFruits() {
      this.fruits = [
        {
          id: 1,
          name: 'Banana',
          color: 'Yellow',
        },
        {
          id: 2,
          name: 'Apple',
          color: 'Red',
        },
        {
          id: 3,
          name: 'Orange',
          color: 'Orange',
        },
        {
          id: 4,
          name: 'Kiwi',
          color: 'Brown',
        },
      ]
    },
    selectFruit(selectedFruit) {
      this.selectedFruit = selectedFruit
    },
    deselectFruit() {
      this.selectedFruit = null
    },
    async addFruit(newFruit) {
      this.fruits.push({
        id: Math.max(0, ...this.fruits.map((fruit) => fruit.id)) + 1,
        ...newFruit,
      })
    },
    async updateFruit(fruitId, updatedValues) {
      Object.assign(
        this.fruits.find((fruit) => fruitId == fruit.id),
        updatedValues,
      )
    },
    async deleteFruit() {
      const fruitIndex = this.fruits.findIndex((fruit) => fruit.id === this.selectedFruit.id)
      this.fruits.splice(fruitIndex, 1)
    },
  },
  mounted() {
    this.fetchFruits()
  },
}
</script>
