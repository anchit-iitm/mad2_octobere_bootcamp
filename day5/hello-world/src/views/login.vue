<template>
    <h3>Login</h3>
    <input type="text" placeholder="email" v-model="this.name">
    <input type="text" placeholder="password" v-model="this.desc">
    <button @click="submit">login</button>
</template>
<script>
import axios from 'axios';

export default {
    name: 'CreateCategory',
    data() {
        return {
            name: null,
            desc: null
        }
    },
    methods: {
        submit() {
            console.log('submit')
            axios
            .post('http://localhost:5000/signin',
                {
                    'email': this.name,
                    'password': this.desc
                }
            )
            .then(response => {
                console.log("correct response", response)
                if (response.data.status == "success in loggin") {
                    localStorage.setItem('authToken', response.data.authToken)
                    this.name = null
                    this.desc = null
                    this.$router.push({name: 'test'})
                }
            })
            .catch(error => {
                console.log("error response", error)
            })
        }
    }
}
</script>