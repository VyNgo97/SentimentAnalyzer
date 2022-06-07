
const fetchMovieData = async () => {
    const data =  await fetch('http://localhost:8000/movies/avengers', {
        method: 'GET',
        cache: 'no-cache',
        headers: {'Content-Type': 'application/json'}
    });
    console.log(data.json())
    return data;
}

export default fetchMovieData;