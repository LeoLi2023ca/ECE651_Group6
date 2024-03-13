// src/store/index.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    user: {
      role: "0"
    }
  },
  mutations: {
    setUserRole(state, role) {
      state.user.role = role;
    }
  },

  getters: {
    userRole: state => state.user.role,
  }
});
