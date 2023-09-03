<script>
import axios from 'axios'

export default {
  data() {
    return {
      activeAddUserModal: false,
      addUserForm: {
        id: '',
        name: '',
        gender: ''
      },
      users: []
    }
  },
  methods: {
    addUser(payload) {
      const path = 'http://localhost:5001/users'
      axios
        .post(path, payload)
        .then(() => {
          this.getUsers()
        })
        .catch((error) => {
          console.error(error)
          this.getUsers()
        })
    },
    getUsers() {
      const path = 'http://localhost:5001/users'
      axios
        .get(path)
        .then((res) => {
          this.users = res.data.users
        })
        .catch((error) => {
          console.error(error)
        })
    },
    handleAddReset() {
      this.initForm()
    },
    handleAddSubmit() {
      this.toggleAddUserModal()
      const payload = {
        id: this.addUserForm.id,
        name: this.addUserForm.name,
        gender: this.addUserForm.gender
      }
      this.addUser(payload)
      this.initForm()
    },
    initForm() {
      this.addUserForm.id = ''
      this.addUserForm.name = ''
      this.addUserForm.gender = ''
    },
    toggleAddUserModal() {
      const body = document.querySelector('body')
      this.activeAddUserModal = !this.activeAddUserModal
      if (this.activeAddUserModal) {
        body.classList.add('modal-open')
      } else {
        body.classList.remove('modal-open')
      }
    }
  },
  created() {
    this.getUsers()
  }
}
</script>

<template>
  <div class="flex justify-between my-10 mx-20 relative overflow-x-auto shadow-md sm:rounded-lg">
    <button type="button" class="btn btn-success btn-sm" @click="toggleAddUserModal">
      Add User
    </button>
    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50">
        <tr>
          <th scope="col" class="px-6 py-3">USER ID</th>
          <th scope="col" class="px-6 py-3">NAME</th>
          <th scope="col" class="px-6 py-3">GENDER</th>
          <th scope="col" class="px-6 py-3"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(user, index) in users" :key="index" class="bg-white border-b hover:bg-gray-50">
          <th
            scope="row"
            class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
          >
            {{ user.id }}
          </th>
          <td class="px-6 py-4">{{ user.name }}</td>
          <td class="px-6 py-4">{{ user.gender }}</td>
          <td class="px-6 py-4 text-right">
            <span>
              <button
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full"
              >
                Edit User
              </button>
            </span>
          </td>
        </tr>
      </tbody>
    </table>
    <!-- Add User Modal -->

    <div
      ref="addUserModal"
      class="modal fade"
      :class="{ show: activeAddUserModal, 'd-block': activeAddUserModal }"
      tabindex="-1"
      role="dialog"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add new user</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="toggleAddUserModal"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="addUserId" class="form-label">Id:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addUserId"
                  v-model="addUserForm.id"
                  placeholder="Enter ID"
                />
              </div>
              <div class="mb-3">
                <label for="addUserName" class="form-label">Name:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addUserName"
                  v-model="addUserForm.name"
                  placeholder="Enter name"
                />
              </div>
              <div>
                <label class="" for="addUserGender">Gender:</label>
              </div>
              <div class="mb-3 form">
                <select
                  selected={value}
                  type="checkbox"
                  class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 rounded leading-tight focus:outline-none"
                  id="addUserGender"
                  v-model="addUserForm.gender"
                >
                  <option value="male">Male</option>
                  <option value="female">Female</option>
                </select>
              </div>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-success btn-sm" @click="handleAddSubmit">
                  Submit
                </button>
                <button type="button" class="btn btn-danger btn-sm" @click="handleAddReset">
                  Reset
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeAddUserModal" class="modal-backdrop fade show"></div>
  </div>
</template>
