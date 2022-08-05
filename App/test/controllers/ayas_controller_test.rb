require "test_helper"

class AyasControllerTest < ActionDispatch::IntegrationTest
  setup do
    @aya = ayas(:one)
  end

  test "should get index" do
    get ayas_url
    assert_response :success
  end

  test "should get new" do
    get new_aya_url
    assert_response :success
  end

  test "should create aya" do
    assert_difference('Aya.count') do
      post ayas_url, params: { aya: { content: @aya.content, number: @aya.number } }
    end

    assert_redirected_to aya_url(Aya.last)
  end

  test "should show aya" do
    get aya_url(@aya)
    assert_response :success
  end

  test "should get edit" do
    get edit_aya_url(@aya)
    assert_response :success
  end

  test "should update aya" do
    patch aya_url(@aya), params: { aya: { content: @aya.content, number: @aya.number } }
    assert_redirected_to aya_url(@aya)
  end

  test "should destroy aya" do
    assert_difference('Aya.count', -1) do
      delete aya_url(@aya)
    end

    assert_redirected_to ayas_url
  end
end
