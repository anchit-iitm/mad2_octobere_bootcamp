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
            </tr>
        </thead>
        <tbody>
            <tr v-for="i in cate">
                <td>{{ i.id }}</td>
                <td>{{i.name}}</td>
                <td>{{i.description}}</td>
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
            cate: null,
            token: null
        }
    },
    created(){
        this.token = localStorage.getItem('authToken')
        this.fetchCate()
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
        }     
    }
}
</script>