import axios from '../../axios-auth'
import Vue from 'vue'



const state = {
    products : [],
    authUser: {},
    isAuthenticated: false,
    jwt: localStorage.getItem('access_token'),
    endpoints: {
      // TODO: Remove hardcoding of dev endpoints
      obtainJWT: 'auth/token/',
      refreshJWT: 'auth/refresh_token/',
    }
};

const getters = {
    allProducts:(state) => state.products,
    authUser:(state)=> state.authUser,
    loggedIn (state) {
      return (state.jwt)
    },
};

const actions = {
    async fetchProducts({commit}){
        const response = await axios.get('store/products/');
        console.log(response.data)
    },
    async fetchLoggedInUser({commit}){
      const response = await axios.get('accounts/user/');
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
    updateToken(state, accessToken,refreshToken) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.setItem('access_token', accessToken);
      localStorage.setItem('refresh_token', refreshToken);
      state.jwt = accessToken;
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

