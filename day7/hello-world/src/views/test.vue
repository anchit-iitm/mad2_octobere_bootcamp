<template>
    <input type="text" placeholder="write the message" v-model="this.msg">
    <button type="button" @click="this.send_testpost_request()">print</button>
    <h1>message: {{ this.msg }}</h1>
    <p v-if="var1">backend respone: {{ this.res }}</p>
    <table v-if="var1">
        <tbody>
            <tr v-for="i in var4">
                <td>{{ i }}</td>
            </tr>
        </tbody>
    </table>
    <table>
        <thead>
            <tr>
                <th>id</th>
                <th>name</th>
                <th>description</th>
                <th>delete_status</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="i in cate">
                <td>{{ i.id }}</td>
                <td>{{i.name}}</td>
                <td>{{i.description}}</td>
                <td>{{i.delete}}</td>
                <td><router-link :to="{'name': 'update', 'params':{'category_id':i.id}}"><Button>update</Button></router-link></td>
                <td><Button @click="delete_category(i.id)">delete</Button></td>
            </tr>
        </tbody>
    </table>
    <table v-if="this.role == 'admin'">
        <thead>
            <tr>
                <th>id</th>
                <th>email</th>
                <th>ative_status</th>
                <th>roles</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="i in users">
                <td>{{ i.id }}</td>
                <td>{{i.email}}</td>
                <td>{{i.active}}</td>
                <td>{{i.roles}}</td>
                <td v-if="i.id != 1"><Button @click="switch_user(i.id)">Switch</Button></td>
            </tr>
        </tbody>
    </table>

</template>
<script>
// from flask import Flask
import axios from 'axios';
export default {
    name: 'testview',
    data(){
        return{
            msg: null,
            res: null,
            var4: null,
            var1: null,
            cate: null, // data for the category is already fetched
            search_field: null, // updated from the input field with v-model
            search_cate: null, // data will be filtered as per the input field, using a method wich is using js filter, use it in the vue lifeccyle hook, beforeupdated
            token: null,
            users: null,
            role: null
        }
    },
    created(){
        this.token = localStorage.getItem('authToken')
        this.role = localStorage.getItem('role')
        console.log(this.role);
        
        if (this.token == null){
            this.$router.push({name: 'login'})
        }
        this.fetchCate()
        if (this.role == 'admin'){
        this.fetchusers()
        }
    },
    methods:{
        print(){
            console.log(this.msg)
            this.msg = null
        },
        send_testpost_request(){
            console.log('send_testpost_request');
            axios
            .post('http://localhost:5000/testapi',
                {
                    message: this.msg
                }
            )
            .then(response => {
                console.log("correct response", response)
                this.msg = null
                this.res = response.data.message
                this.var4 = response.data.var4
                this.var1 = response.data.var1
            })
            .catch(error => {
                console.log("error response", error)
            })
        },
        fetchCate(){
            axios
            .get('http://localhost:5000/api/category',
                {
                    headers: {
                        'Authorization': this.token
                    }
                }
            )
            .then(response => {
                console.log("correct response", response)
                this.cate = response.data.data
            })
            .catch(error => {
                console.log("error response", error)
            })
        },
        delete_category(id){
            axios
            .delete(`http://localhost:5000/api/category/${id}`,
                {
                    headers: {
                        'Authorization': this.token
                    }
                }
            )
            .then(response => {
                // console.log("correct response", response)
                if (response.status == 201){
                    this.fetchCate()
                }
            })
            .catch(error => {
                console.log("error response", error)
            })     
    },
    fetchusers(){
            axios
            .get('http://localhost:5000/api/users',
                {
                    headers: {
                        'Authorization': this.token
                    }
                }
            )
            .then(response => {
                console.log("correct response", response)
                this.users = response.data.data
                console.log(this.users);                
            })
            .catch(error => {
                console.log("error response", error)
            })
        },
        switch_user(id){
            axios
            .put(`http://localhost:5000/api/toggle_user_status/${id}`,
            {},
                {
                    headers: {
                        'Authorization': this.token
                    }
                }
            )
            .then(response => {
                // console.log("correct response", response)
                if (response.status == 201){
                    this.fetchusers()
                }
            })
            .catch(error => {
                console.log("error response", error)
            })     
    },
}
}
</script>