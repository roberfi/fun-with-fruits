<template>
  <div>
    <div class="card">
      <h3 class="fwf-label">List of fruits</h3>
      <div class="grid grid-cols-1 gap-2 h-fit">
        <div
          v-for="fruit in fruits"
          :key="fruit.id"
          class="fwf-list-item"
          :class="fruit == selectedFruit ? 'fwf-active-list-item' : ''"
          @click="updateSelectedFruit(fruit)"
        >
          <div class="flex justify-between items-center">
            <h2 class="text-lg font-medium text-gray-900">{{ fruit.name }}</h2>
            <span class="text-sm font-medium text-gray-500">{{ fruit.color }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FruitsList',
  props: ['selectedFruit'],
  data() {
    return {
      fruits: [],
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
    updateSelectedFruit(selectedFruit) {
      this.$emit('updateSelectedFruit', selectedFruit)
    },
  },
  mounted() {
    this.fetchFruits()
  },
}
</script>
