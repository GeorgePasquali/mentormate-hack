/**
 * GET /
 * Post page.
 */
exports.index = (req, res) => {
    res.render('post', {
      title: 'Post'
    });
  };
  