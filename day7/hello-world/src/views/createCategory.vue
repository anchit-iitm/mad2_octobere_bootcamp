<template>
    <h3>Create Category</h3>
    <input type="text" placeholder="name" v-model="this.name">
    <input type="text" placeholder="desc" v-model="this.desc">
    <button @click="submit">submit</button>
</template>
<script>
import axios from 'axios';

export default {
    name: 'CreateCategory',
    data() {
        return {
            name: null,
            desc: null,
            token: null,
            role: null
        }
    },
    created() {
        this.token = localStorage.getItem('authToken')
        this.role = localStorage.getItem('role')
        if (this.token == null) {
            this.$router.push({name: 'login'});
        }
        console.log(this.role);
        
        if (this.role != 'admin') 
        {
            localStorage.clear();
            this.$router.push({name: 'login'});
        }
    },
    methods: {
        submit() {
            console.log('submit')
            axios
            .post('http://localhost:5000/api/category',
                {
                    'name': this.name,
                    'description': this.desc
                },
                {
                    headers: {
                        'Authorization': this.token
                    }
                }
            )
            .then(response => {
                console.log("correct response", response)
            })
            .catch(error => {
                console.log("error response", error)
            })
        }
    }
}
</script>