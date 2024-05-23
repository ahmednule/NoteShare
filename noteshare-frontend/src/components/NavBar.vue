<template>
    <v-app-bar app color="Grey" dark flat class="px-12">
        <v-btn>
            <v-icon color="Yellow" left class = "mr-2">fas fa-signature</v-icon>NOTESHARE
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn text @click="goToProfile"><v-icon>mdi-account</v-icon></v-btn>
        <v-btn text @click="goToSignUp">Sign Up</v-btn>
        <v-btn text @click="goToLogin">Login</v-btn>
    
    </v-app-bar>
</template>
 
<script>
export default{
    methods:{
        scroll(refName){
            const element = document.getElementById(refName);
            element.scrollIntoView({behavior: 'smooth'});
        },
        goToSignUp(){
            this.router.push('/signup')
        },
        goToProfile(){
            this.$router.push('/profile');  
        },
        goToLogin(){
            this.$router.push('/login');
        }
    }
}

</script>

<style scoped>
nav{
    background-color: black;
    color: white;
    padding: 1rem;
}

</style>