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
import axios from 'axios'

export default {
  name: 'FruitsContainer',
  data() {
    return {
      fruits: [],
      selectedFruit: null,
    }
  },
  methods: {
    selectFruit(selectedFruit) {
      this.selectedFruit = selectedFruit
    },
    deselectFruit() {
      this.selectedFruit = null
    },
    fetchFruits() {
      axios
        .get('/fruits')
        .then((response) => (this.fruits = response.data))
        .catch((error) => console.error('Error fetching fruits:', error))
    },
    addFruit(newFruit) {
      axios
        .post('/fruits', {
          name: newFruit.name,
          color: newFruit.color,
        })
        .then((response) => this.fruits.push(response.data))
        .catch((error) => console.error('Error adding fruit:', error))
    },
    updateFruit(fruitId, updatedValues) {
      axios
        .put('/fruits/' + fruitId, updatedValues)
        .then((response) =>
          Object.assign(
            this.fruits.find((fruit) => fruitId == fruit.id),
            response.data,
          ),
        )
        .catch((error) => console.error('Error updating fruit:', error))
    },
    deleteFruit() {
      const idToDelete = this.selectedFruit.id
      axios
        .delete('/fruits/' + idToDelete)
        .then(() =>
          this.fruits.splice(
            this.fruits.findIndex((fruit) => fruit.id === idToDelete),
            1,
          ),
        )
        .catch((error) => console.error('Error updating fruit:', error))
    },
  },
  mounted() {
    this.fetchFruits()
  },
}
</script>
