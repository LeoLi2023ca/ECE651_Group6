// src/store/index.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    user: {
      role: sessionStorage.getItem('role') || "0"
    }
  },
  mutations: {
    setUserRole(state, role) {
      state.user.role = role;
    },
    resetUserState(state) {
      state.user.role = "0";
    }
  },

  getters: {
    userRole: state => state.user.role,
  },
  actions: {
    signOut({ commit }) {
      sessionStorage.clear();
      commit('resetUserState');
    }
  }
});
