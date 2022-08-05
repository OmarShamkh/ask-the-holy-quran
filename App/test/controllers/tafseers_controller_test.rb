require "test_helper"

class TafseersControllerTest < ActionDispatch::IntegrationTest
  test "should get show" do
    get tafseers_show_url
    assert_response :success
  end

  test "should get index" do
    get tafseers_index_url
    assert_response :success
  end
end
