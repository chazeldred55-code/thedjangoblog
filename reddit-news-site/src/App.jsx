import React, { useState, useEffect } from 'react';
import { ArrowUp, ArrowDown, MessageSquare, Plus, X } from 'lucide-react';

export default function RedditNewsApp() {
  const [posts, setPosts] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [showNewPost, setShowNewPost] = useState(false);
  const [expandedPost, setExpandedPost] = useState(null);
  const [newPost, setNewPost] = useState({
    title: '',
    url: '',
    category: 'general',
    content: ''
  });
  const [newComment, setNewComment] = useState({});

  const categories = [
    'all',
    'technology',
    'politics',
    'science',
    'entertainment',
    'sports',
    'general'
  ];

  useEffect(() => {
    loadPosts();
  }, []);

  const loadPosts = () => {
    try {
      const saved = localStorage.getItem('reddit-posts');
      if (saved) {
        setPosts(JSON.parse(saved));
      }
    } catch (error) {
      console.error('Failed to load posts:', error);
      setPosts([]);
    }
  };

  const savePosts = (updatedPosts) => {
    try {
      localStorage.setItem('reddit-posts', JSON.stringify(updatedPosts));
      setPosts(updatedPosts);
    } catch (error) {
      console.error('Failed to save posts:', error);
    }
  };

  const createPost = () => {
    if (!newPost.title.trim()) return;

    const post = {
      id: Date.now(),
      title: newPost.title,
      url: newPost.url,
      content: newPost.content,
      category: newPost.category,
      votes: 0,
      comments: [],
      timestamp: new Date().toISOString(),
      userVote: 0
    };

    savePosts([post, ...posts]);
    setNewPost({ title: '', url: '', category: 'general', content: '' });
    setShowNewPost(false);
  };

  const vote = (postId, value) => {
    const updatedPosts = posts.map(post => {
      if (post.id === postId) {
        const oldVote = post.userVote || 0;
        const newVote = oldVote === value ? 0 : value;
        return {
          ...post,
          votes: post.votes - oldVote + newVote,
          userVote: newVote
        };
      }
      return post;
    });
    savePosts(updatedPosts);
  };

  const addComment = (postId) => {
    const commentText = newComment[postId];
    if (!commentText?.trim()) return;

    const updatedPosts = posts.map(post => {
      if (post.id === postId) {
        return {
          ...post,
          comments: [
            ...post.comments,
            {
              id: Date.now(),
              text: commentText,
              timestamp: new Date().toISOString()
            }
          ]
        };
      }
      return post;
    });

    savePosts(updatedPosts);
    setNewComment({ ...newComment, [postId]: '' });
  };

  const formatTime = (timestamp) => {
    const now = new Date();
    const posted = new Date(timestamp);
    const diff = Math.floor((now - posted) / 1000);

    if (diff < 60) return 'just now';
    if (diff < 3600) return `${Math.floor(diff / 60)}m ago`;
    if (diff < 86400) return `${Math.floor(diff / 3600)}h ago`;
    return `${Math.floor(diff / 86400)}d ago`;
  };

  const filteredPosts =
    selectedCategory === 'all'
      ? posts
      : posts.filter(p => p.category === selectedCategory);

  const sortedPosts = [...filteredPosts].sort((a, b) => b.votes - a.votes);

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-orange-600 text-white p-4 shadow-lg">
        <div className="max-w-5xl mx-auto flex justify-between items-center">
          <h1 className="text-2xl font-bold">NewsHub</h1>
          <button
            onClick={() => setShowNewPost(true)}
            className="bg-white text-orange-600 px-4 py-2 rounded-full flex items-center gap-2 font-semibold hover:bg-orange-50 transition"
          >
            <Plus size={20} />
            Create Post
          </button>
        </div>
      </header>

      <div className="max-w-5xl mx-auto mt-6 px-4">
        <div className="flex gap-2 mb-6 overflow-x-auto pb-2">
          {categories.map(cat => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              className={`px-4 py-2 rounded-full font-medium whitespace-nowrap transition ${
                selectedCategory === cat
                  ? 'bg-orange-600 text-white'
                  : 'bg-white text-gray-700 hover:bg-gray-50'
              }`}
            >
              {cat.charAt(0).toUpperCase() + cat.slice(1)}
            </button>
          ))}
        </div>

        <div className="space-y-4">
          {sortedPosts.length === 0 ? (
            <div className="bg-white rounded-lg p-8 text-center text-gray-500">
              No posts yet. Be the first to create one!
            </div>
          ) : (
            sortedPosts.map(post => (
              <div
                key={post.id}
                className="bg-white rounded-lg shadow hover:shadow-md transition"
              >
                <div className="flex">
                  <div className="flex flex-col items-center gap-1 p-4 bg-gray-50">
                    <button
                      onClick={() => vote(post.id, 1)}
                      className={`p-1 rounded ${
                        post.userVote === 1
                          ? 'text-orange-600'
                          : 'text-gray-400 hover:text-orange-600'
                      }`}
                    >
                      <ArrowUp size={20} />
                    </button>

                    <span className="font-bold text-gray-700">
                      {post.votes}
                    </span>

                    <button
                      onClick={() => vote(post.id, -1)}
                      className={`p-1 rounded ${
                        post.userVote === -1
                          ? 'text-blue-600'
                          : 'text-gray-400 hover:text-blue-600'
                      }`}
                    >
                      <ArrowDown size={20} />
                    </button>
                  </div>

                  <div className="flex-1 p-4">
                    <h2 className="text-xl font-bold mb-2">
                      {post.title}
                    </h2>

                    {post.content && (
                      <p className="text-gray-700 mb-3">
                        {post.content}
                      </p>
                    )}

                    {post.url && (
                      <a
                        href={post.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-blue-600 hover:underline text-sm mb-3 inline-block"
                      >
                        {post.url}
                      </a>
                    )}

                    <button
                      onClick={() =>
                        setExpandedPost(
                          expandedPost === post.id ? null : post.id
                        )
                      }
                      className="flex items-center gap-2 text-gray-600 hover:text-gray-900 transition"
                    >
                      <MessageSquare size={18} />
                      <span>{post.comments.length} comments</span>
                    </button>

                    {expandedPost === post.id && (
                      <div className="mt-4 pt-4 border-t">
                        <div className="space-y-4 mb-4">
                          {post.comments.map(comment => (
                            <div
                              key={comment.id}
                              className="bg-gray-50 p-3 rounded-lg"
                            >
                              <p className="text-gray-800">
                                {comment.text}
                              </p>
                            </div>
                          ))}
                        </div>

                        <div className="flex gap-2">
                          <input
                            type="text"
                            placeholder="Add a comment..."
                            value={newComment[post.id] || ''}
                            onChange={(e) =>
                              setNewComment({
                                ...newComment,
                                [post.id]: e.target.value
                              })
                            }
                            className="flex-1 p-2 border rounded-lg"
                          />
                          <button
                            onClick={() => addComment(post.id)}
                            className="bg-orange-600 text-white px-4 py-2 rounded-lg"
                          >
                            Comment
                          </button>
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}
