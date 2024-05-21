<template>
    <form>
<label> First Name: </label>
<input type="text" required />
<label> Last Name: </label>
<input type="text" required />
<label> Email: </label>
<input type="email" required />
<Label> Passwword </Label>
<input type="password" required />

<button type="submit" @click='signUp'> Create Account </button>
</form>
</template>
<script>

</script>
<style>
form{
    max-width: 420px;
    margin: 30px auto;
    padding:40px;
    text-align: left;
    background: white;
    border-radius: 10px;

}
label{
    color:rgb(17, 65, 80);
    display:inline-block;
    margin:25px 0 5px;
    font-family: 'Times New Roman', Times, serif;;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;

}
input{
    width: 100%;
    display:block;
    padding: 10px 6px;
    margin: 5px 0;
    box-sizing: border-box;
    border:none;
    border-bottom: 1px solid #ddd;
    color:#555;

    
}
button{
    margin:20px 0;
    padding: 30px;
    max-width: 180px;
    width: 100%;
    border: 2px solid #5f6bd4;
    background: rgb(172, 172, 199);
    border-radius: 10px;
    display: block;
    text-align: center;
    left:90px;
}
</style>