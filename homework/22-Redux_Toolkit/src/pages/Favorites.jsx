import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { removeFavorite } from "../features/favorites/favoritesSlice";

const Favorites = () => {

  const favorites = useSelector(
    (state) => state.favorites.favorites
  );

  const dispatch = useDispatch();

  if (favorites.length === 0) {
    return <h2>No Favorite Movies</h2>;
  }

  return (
    <div>
      <h1>Favorite Movies</h1>

      {favorites.map((movie) => (

        <div key={movie.id}>

          <img
            src={movie.image}
            alt={movie.title}
            width="200"
          />

          <h2>{movie.title}</h2>

          <p>{movie.year}</p>

          <button
            onClick={() =>
              dispatch(removeFavorite(movie.id))
            }
          >
            Remove
          </button>

        </div>
      ))}

    </div>
  )
}

export default Favorites;