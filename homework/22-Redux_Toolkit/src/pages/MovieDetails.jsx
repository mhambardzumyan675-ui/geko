import React from 'react'
import { useParams } from 'react-router-dom'
import movies from '../data/movies'

const MovieDetails = () => {

    const {id}=useParams()

const movie=movies.find((movie)=>movie.id===Number(id))

  return (
    <div>
        <h1>MovieDetails</h1> 
        <div className='movie-card'>
        <img src={movie.image} alt='poster'/>
        <h3>{movie.title}</h3>
        <p>{movie.desc}</p>
        <p>{movie.year}</p>
        <p>{movie.rating}</p>
</div>
    </div>
  )
}

export default MovieDetails