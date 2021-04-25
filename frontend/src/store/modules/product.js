import axios from 'axios'
import Vue from 'vue'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const state = {
    products : [],
    authUser: {},
    isAuthenticated: false,
    jwt: localStorage.getItem('token'),
    endpoints: {
      // TODO: Remove hardcoding of dev endpoints
      obtainJWT: 'http://127.0.0.1:8000/api/v1/auth/obtain_token/',
      refreshJWT: 'http://127.0.0.1:8000/api/v1/auth/refresh_token/',
      baseUrl: 'http://127.0.0.1:8000/api/v1/'
    }
};

const getters = {
    allProducts:(state) => state.products
};

const actions = {
    async fetchProducts({commit}){
        const response = await axios.get('http://127.0.0.1:8000/api/v1/store/products/');
        console.log(response.data)
    }
};

const mutations = {
    setAuthUser(state, {
      authUser,
      isAuthenticated
    }) {
      Vue.set(state, 'authUser', authUser)
      Vue.set(state, 'isAuthenticated', isAuthenticated)
    },
    updateToken(state, newToken) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.setItem('token', newToken);
      state.jwt = newToken;
    },
    removeToken(state) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.removeItem('token');
      state.jwt = null;
    }
  }

export default {
    state,
    getters,
    actions,
    mutations
};

