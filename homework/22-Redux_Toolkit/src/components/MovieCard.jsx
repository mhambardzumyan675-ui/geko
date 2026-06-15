import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { addFavorite } from '../features/favorites/favoritesSlice'
import { Link } from 'react-router-dom'
import "./MovieCard.css"
import movies from '../data/movies'

const MovieCard = ({id,image,title,year}) => {

const dispatch=useDispatch()
const favorites = useSelector((state) => state.favorites.favorites)
const handleAdd=()=>{
const added=favorites.some(movie=>movie.id===id)
if(!added) {
  dispatch(addFavorite({id,title,image,year}))
}
}
  return (
    <>
    <div className='card'>
        <img  className='poster' src={image} alt='poster'/>
        <h3>{title}</h3>
        <p>{year}</p>
        <button onClick={handleAdd}>Add Favorite</button>
        <Link to={`/movies/${id}`}>
        <button>Details</button>
        </Link>
    </div>
    </>
  )
}

export default MovieCard