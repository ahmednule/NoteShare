<template>
    <div class="login-background">
      <v-container class="login-container custom-container">
        <v-row justify="center">
          <v-col cols="12" md="6">
            <v-card class="pa-5 gradient-container">
              <v-card-title class="justify-center">
                <img src="../assets/images/logo1.jpeg" class="logo" alt="Logo" />
              </v-card-title>
              <v-card-subtitle class="text-center">
                <h1>Login</h1>
              </v-card-subtitle>
              <v-form v-model="valid" ref="form">
                <v-text-field
                  v-model="email"
                  :rules="[rules.required, rules.email]"
                  label="Enter Email"
                  required
                ></v-text-field>
                <v-text-field
                  v-model="password"
                  :rules="[rules.required, rules.min(6)]"
                  label="Enter Password"
                  type="password"
                  required
                ></v-text-field>
                <v-btn class="login-button" color="primary" @click="submit">
                  Login
                </v-btn>
              </v-form>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Login',
    data() {
      return {
        valid: false,
        email: '',
        password: '',
        rules: {
          required: value => !!value || 'Required.',
          email: value => {
            const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
            return pattern.test(value) || 'Invalid e-mail.'
          },
          min: v => v.length >= 6 || 'Min 6 characters',
        },
      }
    },
    methods: {
      submit() {
        if (this.$refs.form.validate()) {
          //This is  Mock login logic, replace with real API call
          if (this.email === 'loisa@example.com' && this.password === 'password') {
            localStorage.setItem('user', JSON.stringify({ email: this.email }));
            // Redirects to homepage
            this.$router.push({ name: 'Home' });
          } else {
            alert('Invalid credentials');
          }
        }
      },
    },
  }
  </script>
  
  <style scoped>
  .login-container {
    background-color: #055e64;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .custom-container {
    background-color: #055e64;
    padding: 20px;
  }
  
  .gradient-container {
    background: linear-gradient(to right, #8ecece, rgb(37, 69, 78));
    padding: 20px;
  }
  
  .logo {
    width: 100px;
  }
  
  .pa-5 {
    padding: 20px;
  }
  
  .text-center {
    text-align: center;
  }
  
  .v-card-title, .v-card-subtitle {
    justify-content: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .login-button {
    width: 320px;
    cursor: pointer;
    height: 40px;
    color: #fff;
    border: 1px;
  }
  
  .login-background {
    background: linear-gradient(to right, #006064, #80CBC4);
    padding: 40px 0;
  }
  </style>
  