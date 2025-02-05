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
          @click="selectFruit(fruit)"
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
  props: ['fruits', 'selectedFruit'],
  data() {
    return {}
  },
  methods: {
    selectFruit(selectedFruit) {
      this.$emit('selectFruit', selectedFruit)
    },
  },
}
</script>
