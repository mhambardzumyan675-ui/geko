import React, { useState } from 'react'



const Home = () => {
  const[name,setName]=useState("")
  return (
        <h1>Welcome! {name}</h1>
  )
}

export default Home