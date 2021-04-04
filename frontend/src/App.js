import React, {useEffect, useState} from 'react';
import './App.css';
import Post from './components/Post';
import PostLoading from './components/PostLoading';

function App() {
  const PostLoad = PostLoading(Post);
  const [appState, setAppState] = useState({
    loading: false,
    posts: null,
  });
  // THis methods helps us avoid componentDidMount & DidUpdate
  useEffect(() => {
    setAppState({loading: true});
    const apiUrl = 'http://127.0.0.1:8000/';
    fetch(apiUrl)
    .then((data) => data.json())
    .then((posts) => {
      setAppState({loading: false, posts:posts});
    });
  }, [setAppState]);
  return (
    <div className="App">
      <h1>Latest Posts</h1>
      <PostLoad isLoading={appState.loading} posts={appState.posts} />
    </div>
  )
}

export default App;