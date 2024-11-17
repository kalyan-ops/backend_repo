### Basic Demonstration of our API endpoint:

- End Point for posts ->  GET /api/posts/
- End point for comments -> GET /api/comments/
- End Point for posts ->  POST /api/posts/
- End Point for comments ->  POST /api/comments/

- Response for GET API for posts
{
  "posts": [
    {
      "id": 1,
      "text": "This is a sample post",
      "timestamp": "2024-11-17T10:00:00Z",
      "comment_count": 5,
      "author_username": "john_doe",
      "comments": [
        {
          "id": 1,
          "text": "This is the first comment",
          "timestamp": "2024-11-17T10:05:00Z",
          "author_username": "jane_smith"
        },
        {
          "id": 2,
          "text": "This is the second comment",
          "timestamp": "2024-11-17T10:06:00Z",
          "author_username": "bob_jones"
        },
        {
          "id": 3,
          "text": "This is the third comment",
          "timestamp": "2024-11-17T10:07:00Z",
          "author_username": "alice_brown"
        }
      ]
    },
    {
      "id": 2,
      "text": "Another post example",
      "timestamp": "2024-11-16T09:00:00Z",
      "comment_count": 0,
      "author_username": "susan_miller",
      "comments": []
    }
  ],
  "page": 1,
  "limit": 10,
  "total_posts": 25
}
- Request Body for POST API for posts
{
  "text": "This is a new post",
  "author_username": "john_doe"
}

