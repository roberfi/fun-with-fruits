<template>
  <div>
    <div class="card">
      <div class="mb-5">
        <label for="fruit_name" class="fwf-label">Fruit Name</label>
        <input
          id="fruit_name"
          v-model="fruit_name"
          class="fwf-form-input"
          :disabled="fruit_id !== null"
        />
      </div>
      <div class="mb-5">
        <label for="fruit_color" class="fwf-label">Fruit Color</label>
        <input id="fruit_color" v-model="fruit_color" class="fwf-form-input" />
      </div>
      <div class="flex gap-2">
        <button @click="saveButtonMethod" class="fwf-btn" :class="saveButtonClass">
          {{ saveButtonText }}
        </button>
        <button v-if="fruit_id !== null" @click="deleteFruit" class="fwf-btn fwf-btn-delete">
          Delete
        </button>
        <button @click="deselectFruit" class="fwf-btn fwf-btn-clear ms-auto">Clear</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ApiForm',
  props: ['selectedFruit'],
  data() {
    return {
      fruit_id: null,
      fruit_name: '',
      fruit_color: '',
    }
  },
  methods: {
    addFruit() {
      this.$emit('addFruit', { name: this.fruit_name, color: this.fruit_color })
      this.fruit_color = ''
      this.fruit_name = ''
    },
    updateFruit() {
      this.$emit('updateFruit', this.fruit_id, { color: this.fruit_color })
      this.deselectFruit()
    },
    deleteFruit() {
      this.$emit('deleteFruit')
      this.deselectFruit()
    },
    deselectFruit() {
      this.$emit('deselectFruit')
    },
  },
  computed: {
    saveButtonText() {
      return this.fruit_id !== null ? 'Update' : 'Add'
    },
    saveButtonMethod() {
      return this.fruit_id !== null ? this.updateFruit : this.addFruit
    },
    saveButtonClass() {
      return this.fruit_id !== null ? 'fwf-btn-update' : 'fwf-btn-send'
    },
  },
  watch: {
    selectedFruit: function (selectedFruit) {
      if (selectedFruit) {
        this.fruit_id = selectedFruit.id
        this.fruit_name = selectedFruit.name
        this.fruit_color = selectedFruit.color
      } else {
        this.fruit_id = null
        this.fruit_name = ''
        this.fruit_color = ''
      }
    },
  },
}
</script>
