Rails.application.routes.draw do
  get 'tafseer/:id', to: 'tafseers#show', as: :tafseer
  get 'tafseers' ,to: "tafseers#index"
  get 'search', to:'search#index'
  get 'semantic' , to:'search#semantic'
  resources :ayas
  root to: 'ayas#home'

  # root to: 'search#index'
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
end
 