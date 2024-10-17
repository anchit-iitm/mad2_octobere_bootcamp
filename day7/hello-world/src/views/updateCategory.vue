<template>
    <h3>update Category</h3>
    <input type="text" placeholder="name" v-model="this.name">
    <input type="text" placeholder="desc" v-model="this.desc">
    <button @click="submit">submit</button>
</template>
<script>
import axios from 'axios';

export default {
    name: 'UpdateCategory',
    data() {
        return {
            name: null,
            desc: null,
            token: null,
            role: null,
            id: null
        }
    },
    created() {
        this.token = localStorage.getItem('authToken')
        this.role = localStorage.getItem('role')
        this.id = this.$route.params.category_id
        this.get_cate_details()
        console.log("id", this.id);
        
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
            .put(`http://localhost:5000/api/category/${this.id}`,
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
                if (response.status == "201") {
                    this.$router.push({name: 'test'})
                }
            })
            .catch(error => {
                console.log("error response", error)
            })
        },
        get_cate_details(){
            axios
            .get(`http://localhost:5000/api/category/${this.id}`,
                {
                    headers: {
                        'Authorization': this.token
                    }
                }
            )
            .then(response => {
                console.log("correct response", response)
                this.name = response.data.data.name
                this.desc = response.data.data.description
            })
            .catch(error => {
                console.log("error response", error)
            }) 
        }
    }
}
</script>