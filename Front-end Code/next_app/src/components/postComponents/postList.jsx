import React, { useState } from 'react';
import PostCard from './postCard';
import PostModal from './postModal';
import styles from './postList.module.css';

const IndexPage = () => {
    const [posts, setPosts] = useState([
        { post_id: 1, name: "hello", date: "2022.1.1", title: 'My Post 1', msg: 'hello World' },
        { post_id: 2, summary: 'Summary 2', content: 'Content 2' },
        // 可以根据需要添加更多卡片
    ]);
    const [selectedPost, setSelectedPost] = useState(null);

    const handleCardClick = (post) => {
        setSelectedPost(post);
    };

    const handleCloseModal = () => {
        setSelectedPost(null);
    };

    return (
        <div className={styles.grid}>
            <h1>Posts</h1>
            {posts.map((post) => (
                <PostCard key={post.post_id} post={post} onClick={handleCardClick} />
            ))}
            {selectedPost && <PostModal post={selectedPost} onClose={handleCloseModal} />}
        </div>
    );
};

export default IndexPage;