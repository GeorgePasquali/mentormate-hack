/**
 * GET /
 * Post page.
 */
exports.index = (req, res) => {
    res.render('bills', {
      title: 'BillZ'
    });
  };
  